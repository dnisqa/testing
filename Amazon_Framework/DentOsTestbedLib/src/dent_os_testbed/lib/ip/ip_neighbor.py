# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/ip/neighbor.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest
from dent_os_testbed.lib.ip.linux.linux_ip_neighbor_impl import LinuxIpNeighborImpl
from dent_os_testbed.lib.test_lib_object import TestLibObject


class IpNeighbor(TestLibObject):
    """
    - ip [ OPTIONS ] neigh { COMMAND | help }
    - ip neigh { add | del | change | replace } { ADDR [ lladdr LLADDR ] [ nud STATE ] | proxy ADDR }
     [ dev DEV ] [ router ] [ extern_learn ]
    - ip neigh { show | flush } [ proxy ] [ to PREFIX ] [ dev DEV ] [ nud STATE ] [ vrf NAME ]

    """

    async def _run_command(api, *argv, **kwarg):
        devices = kwarg["input_data"]
        result = list()
        for device in devices:
            for device_name in device:
                device_result = {device_name: dict()}
                # device lookup
                if "device_obj" in kwarg:
                    device_obj = kwarg.get("device_obj", None)[device_name]
                else:
                    if device_name not in pytest.testbed.devices_dict:
                        device_result[device_name] = "No matching device " + device_name
                        result.append(device_result)
                        return result
                    device_obj = pytest.testbed.devices_dict[device_name]
                commands = ""
                if device_obj.os in ["dentos", "cumulus"]:
                    impl_obj = LinuxIpNeighborImpl()
                    for command in device[device_name]:
                        commands += impl_obj.format_command(command=api, params=command)
                        commands += "&& "
                    commands = commands[:-3]

                else:
                    device_result[device_name]["rc"] = -1
                    device_result[device_name]["result"] = "No matching device OS " + device_obj.os
                    result.append(device_result)
                    return result
                device_result[device_name]["command"] = commands
                try:
                    rc, output = await device_obj.run_cmd(
                        ("sudo " if device_obj.ssh_conn_params.pssh else "") + commands
                    )
                    device_result[device_name]["rc"] = rc
                    device_result[device_name]["result"] = output
                    if "parse_output" in kwarg:
                        parse_output = impl_obj.parse_output(
                            command=api, output=output, commands=commands
                        )
                        device_result[device_name]["parsed_output"] = parse_output
                except Exception as e:
                    device_result[device_name]["rc"] = -1
                    device_result[device_name]["result"] = str(e)
                result.append(device_result)
        return result

    async def add(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpNeighbor.add(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'address':'undefined',
                        'lladdr':'undefined',
                        'nud':'undefined',
                        'proxy':'undefined',
                        'device':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        ip neigh { add | del | change | replace } { ADDR [ lladdr LLADDR ]
                 [ nud { permanent | noarp | stale | reachable } ] | proxy ADDR } [ dev DEV ]

        """
        return await IpNeighbor._run_command("add", *argv, **kwarg)

    async def change(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpNeighbor.change(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'address':'undefined',
                        'lladdr':'undefined',
                        'nud':'undefined',
                        'proxy':'undefined',
                        'device':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        ip neigh { add | del | change | replace } { ADDR [ lladdr LLADDR ]
                 [ nud { permanent | noarp | stale | reachable } ] | proxy ADDR } [ dev DEV ]

        """
        return await IpNeighbor._run_command("change", *argv, **kwarg)

    async def replace(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpNeighbor.replace(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'address':'undefined',
                        'lladdr':'undefined',
                        'nud':'undefined',
                        'proxy':'undefined',
                        'device':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        ip neigh { add | del | change | replace } { ADDR [ lladdr LLADDR ]
                 [ nud { permanent | noarp | stale | reachable } ] | proxy ADDR } [ dev DEV ]

        """
        return await IpNeighbor._run_command("replace", *argv, **kwarg)

    async def delete(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpNeighbor.delete(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'address':'undefined',
                        'lladdr':'undefined',
                        'nud':'undefined',
                        'proxy':'undefined',
                        'device':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        ip neigh { add | del | change | replace } { ADDR [ lladdr LLADDR ]
                 [ nud { permanent | noarp | stale | reachable } ] | proxy ADDR } [ dev DEV ]

        """
        return await IpNeighbor._run_command("delete", *argv, **kwarg)

    async def show(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpNeighbor.show(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'proxy':'undefined',
                        'address':'undefined',
                        'device':'undefined',
                        'nud':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        ip neigh { show | flush } [ proxy ] [ to PREFIX ] [ dev DEV ] [ nud STATE ]

        """
        return await IpNeighbor._run_command("show", *argv, **kwarg)

    async def flush(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpNeighbor.flush(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'proxy':'undefined',
                        'address':'undefined',
                        'device':'undefined',
                        'nud':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        ip neigh { show | flush } [ proxy ] [ to PREFIX ] [ dev DEV ] [ nud STATE ]

        """
        return await IpNeighbor._run_command("flush", *argv, **kwarg)