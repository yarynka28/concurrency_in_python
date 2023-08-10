import asyncio
import aiohttp

async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filename = url.split("/")[-1]
                with open(filename, "wb") as file:
                    while chunk := await response.content.read(1024):
                        file.write(chunk)
                print(f"Finished downloading {filename}")
            else:
                print(f"Failed to download file from {url}")

async def main():
    downloads = []

    while True:
        url = input("Please enter the file url to download:\n>")
        if not url:
            break

        task = asyncio.create_task(download_file(url))
        downloads.append(task)
        print(f"Started downloading a file from {url}")
        print(f"Downloading {len(downloads)} files")

    await asyncio.gather(*downloads)

    print("All files finished downloading")

if __name__ == "__main__":
    asyncio.run(main())
