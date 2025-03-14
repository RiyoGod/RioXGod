from RioGod import db
import asyncio

collection = db["afk"]


async def set_afk(afk_status, afk_since, reason):
    doc = {"_id": 1, "afk_status": afk_status, "afk_since": afk_since, "reason": reason}
    r = await collection.find_one({"_id": 1})
    if r:
        await collection.update_one({"_id": 1}, {"$set": doc})
    else:
        await collection.insert_one(doc)


async def set_unafk():
    await collection.update_one(
        {"_id": 1}, {"$set": {"afk_status": False, "afk_since": None, "reason": None}}
    )


async def get_afk_status():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    else:
        return result.get("afk_status", False)


async def afk_stuff():
    result = await collection.find_one({"_id": 1})
    if result:
        afk_since = result.get("afk_since")
        reason = result.get("reason")
        return afk_since, reason
    return None, None
