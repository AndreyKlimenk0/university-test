from sanic.response import json

from service_api.resources import BaseResource
from service_api.domain.subject import get_subject, create_subject, delete_subject
from service_api.forms import SubjectSchema


class SubjectResources(BaseResource):

    async def get(self, request, subject_id):
        subject = await get_subject(subject_id)
        return json({'subject': subject.items()})

    async def post(self, request):
        data = {} if not request.json else request.json.copy()
        data, _ = SubjectSchema(strict=True).dump(data)
        subject = await create_subject(data=data)
        return json({'created_subject': subject.items()})

    async def delete(self, request, subject_id):
        await delete_subject(subject_id)
        return json({'status': 'ok'})
