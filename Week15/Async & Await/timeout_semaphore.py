import asyncio
import random


semaphore = asyncio.Semaphore(5)


async def fake_api_call(document_id):
    """Pretend this is an HTTP API call."""
    delay = random.uniform(0.5, 5.0)

    print(f"Request {document_id}: starting ({delay:.1f}s)")
    await asyncio.sleep(delay)

    return f"Document {document_id} downloaded"


async def fetch_document(document_id):
    # Only 5 tasks can enter this section simultaneously.
    async with semaphore:
        try:
            # This particular API request gets at most 3 seconds.
            async with asyncio.timeout(3):
                result = await fake_api_call(document_id)

                print(f"Request {document_id}: success")
                return result

        except TimeoutError:
            print(f"Request {document_id}: TIMEOUT")
            return None

        finally:
            print(f"Request {document_id}: cleanup")


async def main():
    document_ids = range(1, 21)

    # Create many concurrent tasks.
    tasks = [
        asyncio.create_task(fetch_document(doc_id))
        for doc_id in document_ids
    ]

    # Wait for all of them to finish.
    results = await asyncio.gather(*tasks)

    successful = [r for r in results if r is not None]

    print(f"\nDownloaded {len(successful)}/{len(document_ids)} documents")


asyncio.run(main())
