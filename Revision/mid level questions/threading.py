import threading
import time

results = {}

def fetch_data(task_id, duration):
    time.sleep(duration)
    results[task_id] = f"Task {task_id} done in {duration}s"

tasks = [(1, 1.5), (2, 0.8), (3, 1.2)]

threads = [
    threading.Thread(target=fetch_data, args=(tid, dur))
    for tid, dur in tasks
]

start = time.time()
for t in threads: t.start()
for t in threads: t.join()
elapsed = time.time() - start

for r in results.values(): print(r)
print(f"Total time: {elapsed:.2f}s (not {sum(d for _,d in tasks)}s)")