# Teja P C

I contribute Python fixes to Microsoft, Apache, Hugging Face, Ray and Dagster. MS CS at UNT.

I work on Python debugging and ML pipelines — the debugger, the triggerer, data loading, and the data that comes out of a model.

These are the changes I have open with big-corps' teams right now.

- [A cold-start test in the VS Code Python debugger](https://github.com/microsoft/vscode-python-debugger/pull/1150). The first test could time out and leave work running into the second. My patch uses the suite's shared timeout. Open, approved.
- [Restoring the terminal when a debuggee exits](https://github.com/microsoft/debugpy/pull/2096). The Python program had exited, but the next shell prompt still had trouble reading the terminal. Open.
- [Uploading finished trigger logs off the Airflow triggerer's event loop](https://github.com/apache/airflow/pull/77290). A finished trigger could still keep the triggerer busy. Open.
- [Flushing staged data when an Arrow writer closes](https://github.com/huggingface/datasets/pull/9104). A small batch made me look twice at what closing an Arrow writer guarantees. Open.

My one merged fix outside these teams is [Headroom's read-only setting](https://github.com/headroomlabs-ai/headroom/pull/4895) — one compression path still recorded an observation when a request was set to read-only.

Follow along if you like short write-ups about debugging Python tools and checking the data that comes out of a model.
