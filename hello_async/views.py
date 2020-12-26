import asyncio
import random
from time import sleep
from typing import List

import httpx
from asgiref.sync import sync_to_async
from django.http import HttpResponse


# helpers

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


# helpers for smoke_some_meats

async def smoke(smokables: List[str] = None, flavor: str = "Sweet Baby Ray's") -> List[str]:
    """ Smokes some meats and applies the Sweet Baby Ray's """

    for smokable in smokables:
        print(f"Smoking some {smokable}...")
        print(f"Applying the {flavor}...")
        print(f"{smokable.capitalize()} smoked.")

    return len(smokables)


async def get_smokables():
    print("Getting smokeables...")

    await asyncio.sleep(2)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")

        print("Returning smokeable")
        return [
            "ribs",
            "brisket",
            "lemon chicken",
            "salmon",
            "bison sirloin",
            "sausage",
        ]


async def get_flavor():
    print("Getting flavor...")

    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")

        print("Returning flavor")
        return random.choice(
            [
                "Sweet Baby Ray's",
                "Stubb's Original",
                "Famous Dave's",
            ]
        )


# helper for smoke_some_meats2
async def smoke2(smokables: List[str] = None, flavor: str = "Sweet Baby Ray's") -> None:
    """  2 Smokes some meats and applies the Sweet Baby Ray's """
    if smokables is None:
        smokables = [
            "ribs",
            "brisket",
            "lemon chicken",
            "salmon",
            "bison sirloin",
            "sausage",
        ]
    if (loved_smokable := smokables[0]) == "ribs":
        loved_smokable = "meats"
    for smokable in smokables:
        print(f"Smoking some {smokable}....")
        await asyncio.sleep(1)
        print(f"Applying the {flavor}....")
        await asyncio.sleep(1)
        print(f"{smokable.capitalize()} smoked.")
    print(f"Who doesn't love smoked {loved_smokable}?")


# helper for burn_some_meats
def oversmoke() -> None:
    """ If it's not dry, it must be uncooked """
    sleep(5)
    print("Who doesn't love burnt meats?")


# views

async def index(request):
    return HttpResponse("Hello, async Django!")


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")


async def smoke_some_meats(request):
    results = await asyncio.gather(*[get_smokables(), get_flavor()])
    total = await asyncio.gather(*[smoke(results[0], results[1])])
    return HttpResponse(f"Smoked {total[0]} meats with {results[1]}!")


async def smoke_some_meats2(request) -> HttpResponse:
    loop = asyncio.get_event_loop()
    smoke_args = []

    if to_smoke := request.GET.get("to_smoke"):
        # Grab smokables
        to_smoke = to_smoke.split(",")
        smoke_args += [[smokable.lower().strip() for smokable in to_smoke]]

        # Do some string prettification
        if (smoke_list_len := len(to_smoke)) == 2:
            to_smoke = " and ".join(to_smoke)
        elif smoke_list_len > 2:
            to_smoke[-1] = f"and {to_smoke[-1]}"
            to_smoke = ", ".join(to_smoke)
    else:
        to_smoke = "meats"

    if flavor := request.GET.get("flavor"):
        smoke_args.append(flavor)

    loop.create_task(smoke2(*smoke_args))
    return HttpResponse(f"Smoking some {to_smoke}....")


async def burn_some_meats(request):
    oversmoke()     # call sync func
    return HttpResponse(f"Burned some meats.")


async def async_with_sync_view(request):
    loop = asyncio.get_event_loop()
    async_function = sync_to_async(http_call_sync)
    loop.create_task(async_function())
    return HttpResponse("Non-blocking HTTP request (via sync_to_async)")
