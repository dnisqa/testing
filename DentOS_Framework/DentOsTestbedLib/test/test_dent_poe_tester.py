# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/poe_tester/poe_tester.yaml
#
# DONOT EDIT - generated by diligent bots

import asyncio

from dent_os_testbed.lib.poe_tester.poe_tester import PoeTester

from .utils import TestDevice


def test_that_poe_tester_attach(capfd):

    dv1 = TestDevice(platform="dni")
    dv2 = TestDevice(platform="dni")
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.attach(
            input_data=[
                {
                    # device 1
                    "test_dev": [{}],
                }
            ],
            device_obj={"test_dev": dv1},
        )
    )
    print(out)
    assert "command" in out[0]["test_dev"].keys()
    assert "result" in out[0]["test_dev"].keys()
    # check the rc
    assert out[0]["test_dev"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.attach(
            input_data=[
                {
                    # device 1
                    "test_dev1": [
                        {
                            # command 1
                            "hostname": "alzsbwuf",
                            "serial_dev": "zjhbfbza",
                            "baudrate": 5583,
                        },
                        {
                            # command 2
                            "hostname": "mpuusyrd",
                            "serial_dev": "bbpcmzde",
                            "baudrate": 2170,
                        },
                    ],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.attach(
            input_data=[
                {
                    # device 1
                    "test_dev1": [
                        {
                            "hostname": "alzsbwuf",
                            "serial_dev": "zjhbfbza",
                            "baudrate": 5583,
                        }
                    ],
                    # device 2
                    "test_dev2": [
                        {
                            "hostname": "mpuusyrd",
                            "serial_dev": "bbpcmzde",
                            "baudrate": 2170,
                        }
                    ],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    assert "command" in out[1]["test_dev2"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    assert "result" in out[1]["test_dev2"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0
    assert out[1]["test_dev2"]["rc"] == 0


def test_that_poe_tester_detach(capfd):

    dv1 = TestDevice(platform="dni")
    dv2 = TestDevice(platform="dni")
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.detach(
            input_data=[
                {
                    # device 1
                    "test_dev": [{}],
                }
            ],
            device_obj={"test_dev": dv1},
        )
    )
    print(out)
    assert "command" in out[0]["test_dev"].keys()
    assert "result" in out[0]["test_dev"].keys()
    # check the rc
    assert out[0]["test_dev"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.detach(
            input_data=[
                {
                    # device 1
                    "test_dev1": [
                        {
                            # command 1
                            "hostname": "lxgmhxjj",
                            "serial_dev": "uveeaohz",
                            "baudrate": 3681,
                        },
                        {
                            # command 2
                            "hostname": "lycanzmw",
                            "serial_dev": "ersyaets",
                            "baudrate": 6999,
                        },
                    ],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.detach(
            input_data=[
                {
                    # device 1
                    "test_dev1": [
                        {
                            "hostname": "lxgmhxjj",
                            "serial_dev": "uveeaohz",
                            "baudrate": 3681,
                        }
                    ],
                    # device 2
                    "test_dev2": [
                        {
                            "hostname": "lycanzmw",
                            "serial_dev": "ersyaets",
                            "baudrate": 6999,
                        }
                    ],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    assert "command" in out[1]["test_dev2"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    assert "result" in out[1]["test_dev2"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0
    assert out[1]["test_dev2"]["rc"] == 0


def test_that_poe_tester_configure_port(capfd):

    dv1 = TestDevice(platform="dni")
    dv2 = TestDevice(platform="dni")
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.configure_port(
            input_data=[
                {
                    # device 1
                    "test_dev": [{}],
                }
            ],
            device_obj={"test_dev": dv1},
        )
    )
    print(out)
    assert "command" in out[0]["test_dev"].keys()
    assert "result" in out[0]["test_dev"].keys()
    # check the rc
    assert out[0]["test_dev"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.configure_port(
            input_data=[
                {
                    # device 1
                    "test_dev1": [
                        {
                            # command 1
                            "input_data": "pzscttqe",
                        },
                        {
                            # command 2
                            "input_data": "evpidszt",
                        },
                    ],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.configure_port(
            input_data=[
                {
                    # device 1
                    "test_dev1": [
                        {
                            "input_data": "pzscttqe",
                        }
                    ],
                    # device 2
                    "test_dev2": [
                        {
                            "input_data": "evpidszt",
                        }
                    ],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    assert "command" in out[1]["test_dev2"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    assert "result" in out[1]["test_dev2"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0
    assert out[1]["test_dev2"]["rc"] == 0


def test_that_poe_tester_get_port_stats(capfd):

    dv1 = TestDevice(platform="dni")
    dv2 = TestDevice(platform="dni")
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.get_port_stats(
            input_data=[
                {
                    # device 1
                    "test_dev": [{}],
                }
            ],
            device_obj={"test_dev": dv1},
        )
    )
    print(out)
    assert "command" in out[0]["test_dev"].keys()
    assert "result" in out[0]["test_dev"].keys()
    # check the rc
    assert out[0]["test_dev"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.get_port_stats(
            input_data=[
                {
                    # device 1
                    "test_dev1": [
                        {
                            # command 1
                        },
                        {
                            # command 2
                        },
                    ],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        PoeTester.get_port_stats(
            input_data=[
                {
                    # device 1
                    "test_dev1": [{}],
                    # device 2
                    "test_dev2": [{}],
                }
            ],
            device_obj={"test_dev1": dv1, "test_dev2": dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert "command" in out[0]["test_dev1"].keys()
    assert "command" in out[1]["test_dev2"].keys()
    # check if the result was formed
    assert "result" in out[0]["test_dev1"].keys()
    assert "result" in out[1]["test_dev2"].keys()
    # check the rc
    assert out[0]["test_dev1"]["rc"] == 0
    assert out[1]["test_dev2"]["rc"] == 0
