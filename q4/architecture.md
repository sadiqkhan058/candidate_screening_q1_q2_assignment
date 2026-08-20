# Q4 Architecture

```text
             Replayed call / future live ASR
                         |
                         v
               Streaming transcript
                         |
                         v
                 Signal extraction
                  /      |       \
                 /       |        \
          sales/compliance sentiment/collections
                         |
                         v
                Confidence threshold
                         |
                         v
             Cooldown + duplicate filter
                         |
                         v
                   Nudge event
                         |
                         v
                  Live dashboard
```

The design keeps signal detection separate from presentation so the same engine can later feed WebSocket, webhook, polling API, or command-line consumers.
