# Optimized Singly Linked List (High-Performance Data Queue)

A production-grade, object-oriented implementation of a Singly Linked List in Python. This module is architected as a highly efficient, sequential memory manager designed to handle high-frequency data ingestion pipelines with minimal overhead.

## 🚀 Architectural Optimization: From $O(N)$ to $O(1)$

In standard singly linked list implementations, appending a new node to the end of the chain is a linear operation ($O(N)$), requiring a traversal loop to crawl from the `head` anchor down to the final node. 

This implementation optimizes the insertion bottleneck down to **$O(1)$ Constant Time** by integrating a twin-anchor architecture utilizing a permanent `tail` pointer tracking system. 

### Performance Reality Check

| Operation | Time Complexity | Space Complexity | Algorithmic Mechanism |
| :--- | :--- | :--- | :--- |
| **Insert at Front** | $O(1)$ Constant | $O(1)$ | Direct pointer reassignment at the `head` anchor. |
| **Insert at End** | **$O(1)$ Constant** | $O(1)$ | Bypasses traversal loops completely by directly mapping to the `tail` anchor. |
| **Delete Value** | $O(N)$ Linear | $O(1)$ | Sequential crawling with single-pass surgical pointer-bypassing. |
| **Print/Stream** | $O(N)$ Linear | $O(1)$ | Linear dynamic crawler tracking sequential addresses. |

---

## 🛠️ Key Engineering Features

* **Encapsulated Class Interface:** Separates individual element construction (`Node`) from the global pipeline tracking layout (`Linked_list`), abstracting memory pointer manipulation away from the execution scope.
* **Memory Safety Guardrails:** The deletion engine is explicitly guarded against `NoneType` pointer violations. If a requested value is absent from system RAM, the boundary conditions catch the empty address and skip execution without interrupting runtime stability or throwing crashes.
* **Native Execution Guard:** Includes standard Python namespace shielding (`if __name__ == "__main__":`) to prevent testing code from execution when imported into a separate microservice pipeline.

---

## 💻 Technical Implementation Details

### System Environment
* **Language:** Python 3.x
* **Paradigm:** Object-Oriented Programming (OOP)
* **Dependencies:** None (Pure Standard Library Implementation)

### File Structure
```text
├── singly_linked_list.py   # Core architecture (Node & Linked_list classes)
└── README.md               # Technical documentation