from datetime import datetime
import time
import asyncio

async def Clock():
    print("\n\n");
    while True:
        print(datetime.now().strftime("\033[A\033[A \rDate: %d-%b-%Y \nTime: %H:%M:%S\n"),end="");
        await asyncio.sleep(1);

if __name__ == "__main__":
    try:
        asyncio.run(Clock());
    except KeyboardInterrupt:
        print("\n");
        print("\nClock Stopped")
