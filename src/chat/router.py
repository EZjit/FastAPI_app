from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.chat.models import Message
from src.db import async_session_maker, get_async_session

router = APIRouter(prefix='/chat', tags=['Chat'])


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    @staticmethod
    async def send_personal_message(message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, add_to_db: bool):
        if add_to_db:
            await self.save_message(message)
        for connection in self.active_connections:
            await connection.send_text(message)

    @staticmethod
    async def save_message(message: str):
        async with async_session_maker() as session:
            statement = insert(Message).values(message=message)
            await session.execute(statement)
            await session.commit()


manager = ConnectionManager()


@router.get('/last_messages')
async def get_last_messages(session: AsyncSession = Depends(get_async_session)):
    query = select(Message).order_by(Message.id.desc()).limit(5)
    result = await session.execute(query)
    return result.scalars().all()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)
