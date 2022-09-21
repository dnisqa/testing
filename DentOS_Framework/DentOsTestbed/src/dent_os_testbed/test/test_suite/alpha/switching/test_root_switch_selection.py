# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#

import json
import time

import pytest

from dent_os_testbed.Device import DeviceType
from dent_os_testbed.utils.test_utils.tb_utils import tb_get_all_devices

pytestmark = pytest.mark.suite_switching


@pytest.mark.asyncio
async def test_alpha_lab_switching_root_switch_selection(testbed):
    """
    Test Name: test_alpha_lab_switching_root_switch_selection
    Test Suite: suite_switching
    Test Overview: test switch root switch selection
    Test Procedure:
    1. Validate root switch selection
    2. Configure different values for switch priority
    3. Validate root changes occur gracefully.
    4. mstpctl settreeportprio bridge 100
    """
    for dd in await tb_get_all_devices(testbed):
        if dd.type != DeviceType.INFRA_SWITCH:
            continue
        # do this on infra switches only
        for cmd in [
            "brctl delbr test_br || true",
            "brctl addbr test_br",
            "brctl stp test_br on",
        ]:
            rc, out = await dd.run_cmd(cmd, sudo=True)
            assert rc == 0, f"failed to run {cmd} rc {rc} out {out}"

        tmpswp = []
        i=0

        for dd2, links in dd.links_dict.items():
            if (
                dd2 not in testbed.devices_dict
                or testbed.devices_dict[dd2].type != DeviceType.INFRA_SWITCH
            ):
                continue
            for swp in links[0]:
                cmd = f"bridge -j link show dev {swp}"
                rc, out = await dd.run_cmd(cmd, sudo=True)
                assert rc == 0, f"failed to run {cmd} rc {rc} out {out}"
                # delete from the old bridge if any
                data = json.loads(out)
                if data and "master" in data[0]:
                    br = data[0]["master"]
                    cmd = f"brctl delif {br} {swp}"
                    rc, out = await dd.run_cmd(cmd, sudo=True)
                    assert rc == 0, f"failed to run {cmd} rc {rc} out {out}"
                tmpswp.append(swp)
                dd.applog.info(f"Recorded bond0 orignal swp port member to list: {tmpswp[i]}")
                i=i+1
                for cmd in [
                    f"ip link set {swp} nomaster",
                    f"brctl addif test_br {swp}",
                    f"ip link set {swp} up",
                ]:
                    rc, out = await dd.run_cmd(cmd, sudo=True)
                    assert rc == 0, f"failed to run {cmd} rc {rc} out {out}"
        for cmd in [
            f"brctl setportprio test_br port prio 256",
            f"brctl show test_br",
            f"brctl showstp test_br",
            f"brctl delbr test_br",
            f"ip link set bond0 nomaster",                                                                                               
            f"ip link set bond0 down",
        ]:
            rc, out = await dd.run_cmd(cmd, sudo=True)
            dd.applog.info(f"Ran command {cmd} rc {rc} out {out}")
        # check the output
        # TODO check for stp state

        i=0
        for i in range(len(tmpswp)):
            dd.applog.info(f"Re-add swp to bond0 info: {tmpswp[i]}")
            cmd = f"bridge -j link show dev {tmpswp[i]}"
            rc, out = await dd.run_cmd(cmd, sudo=True)
            dd.applog.info(f"Ran command {cmd} rc {rc} out {out}")
            assert rc == 0, f"failed to run {cmd} rc {rc} out {out}"
            for cmd in [
                f"ip link set {tmpswp[i]} down",
                f"ip link set {tmpswp[i]} master bond0",
                f"ip link set {tmpswp[i]} up",
            ]:
                rc, out = await dd.run_cmd(cmd, sudo=True)
                dd.applog.info(f"Ran {cmd} with rc {rc} {out}")

        for cmd in [
            f"ip link set bond0 down",
            f"ip link set bond0 up",
            f"ip link set bond0 master bridge",
            f"bridge vlan add vid 100 dev bond0",
            f"bridge vlan add vid 300 dev bond0",
            f"bridge vlan add vid 400 dev bond0",
            f"bridge vlan add vid 500 dev bond0",
            f"bridge vlan add vid 600 dev bond0",
        ]:
            rc, out = await dd.run_cmd(cmd, sudo=True)
            dd.applog.info(f"Ran {cmd} with rc {rc} {out}")

