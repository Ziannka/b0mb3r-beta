from service import Service


class Sunlight(Service):
    async def run(self):
        await self.client.options('https://api.sunlight.net/v3/customers/authorization/')
        await self.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': self.formatted_phone})
