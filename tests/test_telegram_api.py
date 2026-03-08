from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import httpx

from telegras import telegram_api


@pytest.mark.asyncio
async def test_get_file_direct_url_success() -> None:
    """Test successful retrieval of direct file URL."""
    file_id = "test_file_id_123"
    expected_file_path = "photos/file_123.jpg"
    bot_token = "test_bot_token"

    # Mock the _client() to return a client with the bot_token
    mock_client = MagicMock()
    mock_client.bot_token = bot_token
    mock_client.base_url = f"https://api.telegram.org/bot{bot_token}"

    # Mock httpx.AsyncClient context manager
    mock_http_client = AsyncMock()
    mock_response = AsyncMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = {
        "ok": True,
        "result": {
            "file_id": file_id,
            "file_path": expected_file_path,
        }
    }
    mock_http_client.get = AsyncMock(return_value=mock_response)

    with patch.object(telegram_api, "_client", return_value=mock_client):
        with patch("httpx.AsyncClient") as MockAsyncClient:
            MockAsyncClient.return_value.__aenter__.return_value = mock_http_client
            url = await telegram_api.get_file_direct_url(file_id)

    expected_url = f"https://api.telegram.org/file/bot{bot_token}/{expected_file_path}"
    assert url == expected_url

    # Verify the correct parameters were used
    mock_http_client.get.assert_called_once_with(
        f"https://api.telegram.org/bot{bot_token}/getFile",
        params={"file_id": file_id},
        timeout=10.0
    )
    mock_response.raise_for_status.assert_called_once()


@pytest.mark.asyncio
async def test_get_file_direct_url_api_error() -> None:
    """Test get_file_direct_url when Telegram API returns an error."""
    file_id = "test_file_id_123"
    bot_token = "test_bot_token"

    # Mock the _client()
    mock_client = MagicMock()
    mock_client.bot_token = bot_token
    mock_client.base_url = f"https://api.telegram.org/bot{bot_token}"

    # Mock httpx.AsyncClient to return an error response
    mock_http_client = AsyncMock()
    mock_response = AsyncMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = {
        "ok": False,
        "description": "Bad Request: file not found"
    }
    mock_http_client.get = AsyncMock(return_value=mock_response)

    with patch.object(telegram_api, "_client", return_value=mock_client):
        with patch("httpx.AsyncClient") as MockAsyncClient:
            MockAsyncClient.return_value.__aenter__.return_value = mock_http_client
            url = await telegram_api.get_file_direct_url(file_id)

    assert url is None


@pytest.mark.asyncio
async def test_download_file_success() -> None:
    """Test successful file download."""
    file_url = "https://api.telegram.org/file/bot123/photos/file.jpg"
    expected_content = b"fake image content here"

    # Mock httpx.AsyncClient
    mock_http_client = AsyncMock()
    mock_response = AsyncMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.content = expected_content
    mock_http_client.get = AsyncMock(return_value=mock_response)

    with patch("httpx.AsyncClient") as MockAsyncClient:
        MockAsyncClient.return_value.__aenter__.return_value = mock_http_client
        content = await telegram_api.download_file(file_url)

    assert content == expected_content
    mock_http_client.get.assert_called_once_with(file_url, timeout=30.0)
    mock_response.raise_for_status.assert_called_once()


@pytest.mark.asyncio
async def test_download_file_http_error() -> None:
    """Test download_file when HTTP request fails."""
    file_url = "https://api.telegram.org/file/bot123/photos/file.jpg"

    # Mock httpx.AsyncClient to raise HTTP error
    mock_http_client = AsyncMock()
    mock_response = AsyncMock()
    mock_response.raise_for_status = MagicMock(side_effect=httpx.HTTPStatusError(
        "Not Found",
        request=MagicMock(),
        response=MagicMock(status_code=404)
    ))
    mock_http_client.get = AsyncMock(return_value=mock_response)

    with patch("httpx.AsyncClient") as MockAsyncClient:
        MockAsyncClient.return_value.__aenter__.return_value = mock_http_client
        with pytest.raises(httpx.HTTPStatusError):
            await telegram_api.download_file(file_url)

    mock_http_client.get.assert_called_once_with(file_url, timeout=30.0)
