"""Common fixtures for the Lutron Homeworks Series 4 and 8 tests."""
from collections.abc import Generator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from homeassistant.components.homeworks.const import (
    CONF_ADDR,
    CONF_CONTROLLER_ID,
    CONF_DIMMERS,
    CONF_KEYPADS,
    CONF_RATE,
    DOMAIN,
)
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT

from tests.common import MockConfigEntry


@pytest.fixture
def mock_config_entry() -> MockConfigEntry:
    """Return the default mocked config entry."""
    return MockConfigEntry(
        title="Lutron Homeworks",
        domain=DOMAIN,
        data={},
        options={
            CONF_CONTROLLER_ID: "main_controller",
            CONF_HOST: "192.168.0.1",
            CONF_PORT: 1234,
            CONF_DIMMERS: [
                {
                    CONF_ADDR: "[02:08:01:01]",
                    CONF_NAME: "Foyer Sconces",
                    CONF_RATE: 1.0,
                }
            ],
            CONF_KEYPADS: [
                {
                    CONF_ADDR: "[02:08:02:01]",
                    CONF_NAME: "Foyer Keypad",
                }
            ],
        },
    )


@pytest.fixture
def mock_empty_config_entry() -> MockConfigEntry:
    """Return a mocked config entry with no keypads or dimmers."""
    return MockConfigEntry(
        title="Lutron Homeworks",
        domain=DOMAIN,
        data={},
        options={
            CONF_CONTROLLER_ID: "main_controller",
            CONF_HOST: "192.168.0.1",
            CONF_PORT: 1234,
            CONF_DIMMERS: [],
            CONF_KEYPADS: [],
        },
    )


@pytest.fixture
def mock_homeworks() -> Generator[None, MagicMock, None]:
    """Return a mocked Homeworks client."""
    with patch(
        "homeassistant.components.homeworks.Homeworks", autospec=True
    ) as homeworks_mock, patch(
        "homeassistant.components.homeworks.config_flow.Homeworks", new=homeworks_mock
    ):
        yield homeworks_mock


@pytest.fixture
def mock_setup_entry() -> Generator[AsyncMock, None, None]:
    """Override async_setup_entry."""
    with patch(
        "homeassistant.components.homeworks.async_setup_entry", return_value=True
    ) as mock_setup_entry:
        yield mock_setup_entry
