from http.client import HTTPResponse

import aiohttp
import pytest


class CatViewRequests:
    url: str = 'http://127.0.0.1:8000'

    color: str = 'gray'
    age_in_month: int = 0
    edited_age_in_month: int = 1
    description: str = 'test description'
    edited_description: str = 'edited test description'
    breed_id: int = 1

    cat_id: int

    async def create_cat(self) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            response = await session.post(self.url + '/cats/create',
                                          json={
                                              "color": self.color,
                                              "age_in_month": self.age_in_month,
                                              "description": self.description,
                                              "breed_id": self.breed_id
                                          })
            response_data = await response.json()
            self.cat_id = response_data['cat_id']
            return response

    async def edit_cat(self) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.patch(self.url + '/cats/edit',
                                       json={
                                           "cat_id": self.cat_id,
                                           "age_in_month": self.edited_age_in_month,
                                           "description": self.edited_description
                                       })

    async def delete_cat(self) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.delete(self.url + '/cats/delete',
                                        json={
                                            "cat_id": self.cat_id,
                                        })


cat_view_requests = CatViewRequests()

class TestCatViews:
    @pytest.mark.asyncio
    async def test_create_cat(self):
        response = await cat_view_requests.create_cat()
        response_data = await response.json()

        assert response.status == 201
        assert response_data['color'] == cat_view_requests.color
        assert response_data['age_in_month'] == cat_view_requests.age_in_month
        assert response_data['description'] == cat_view_requests.description

    @pytest.mark.asyncio
    async def test_edit_cat(self):
        response = await cat_view_requests.edit_cat()
        response_data = await response.json()

        assert response.status == 200
        assert response_data['color'] == cat_view_requests.color
        assert response_data['age_in_month'] == cat_view_requests.edited_age_in_month
        assert response_data['description'] == cat_view_requests.edited_description

    @pytest.mark.asyncio
    async def test_delete_cat(self):
        response = await cat_view_requests.delete_cat()
        response_data = await response.json()

        assert response.status == 200
