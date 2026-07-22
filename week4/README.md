# Week 4 — Game AI with Minimax Algorithm

## 📌 Overview

สัปดาห์ที่ 4 เรียนรู้การสร้าง **Game AI** ด้วย **Minimax Algorithm** ซึ่งเป็นอัลกอริทึมที่ใช้ในการตัดสินใจในเกมแบบ 2 ผู้เล่น โดย AI จะเลือกการเดินที่ดีที่สุด (optimal play) ทุกครั้ง

## 🎮 Games

### 🪙 Coin Game — `coingame.py`

เกมหยิบเหรียญ (Nim-style Game)

- เริ่มต้นมี **10 เหรียญ**
- แต่ละเทิร์นหยิบได้ **1 หรือ 2 เหรียญ**
- ผู้เล่นที่ทำให้เหรียญหมด **เป็นฝ่ายชนะ**
- AI ใช้ Minimax หาการหยิบที่ดีที่สุด

**วิธีเล่น:**

```bash
python coingame.py
```

---

### 🪙 Coin Game (First Move Check) — `coingame_first_move.py`

ตรวจสอบว่าผู้เล่นคนแรกควรหยิบกี่เหรียญในการเดินครั้งแรกเพื่อ **การันตีชัยชนะ**

- รับจำนวนเหรียญเป็น input
- ถ้าหยิบ **1 เหรียญ** แล้วชนะ → print `1`
- ถ้าหยิบ **2 เหรียญ** แล้วชนะ → print `2`
- ถ้า **ไม่มีทางชนะ** ไม่ว่าจะหยิบ 1 หรือ 2 → print `0`

**วิธีใช้:**

```bash
python coingame_first_move.py
```

---

### ❌⭕ Tic-Tac-Toe — `tictoe.py`

เกม OX เวอร์ชันเต็มแบบ interactive

- ผู้เล่นเป็น `X`, AI เป็น `O`
- ใช้ Minimax Algorithm ให้ AI เล่นอย่างสมบูรณ์แบบ
- มี board display, input validation, และ random first move optimization

**วิธีเล่น:**

```bash
python tictoe.py
```

**Input:** ใส่ตำแหน่ง row และ column (0-2) คั่นด้วย space เช่น `1 1`

---

### ❌⭕ Tic-Tac-Toe (Submission) — `tr.py`

เวอร์ชัน submission สำหรับส่งงาน

- รับ board state 3 บรรทัดเป็น input (ใช้ `X`, `O`, `_`)
- หาตำแหน่งที่ดีที่สุดสำหรับ `X` ด้วย Minimax
- Output: ตำแหน่ง 0-8 (row × 3 + col)

**ตัวอย่าง:**

```
Input:        Output:
X_O           4
___
___
```

---

### ❌⭕ Tic-Tac-Toe (Batch) — `tr copy.py`

เวอร์ชัน batch — รับหลาย board พร้อมกัน

- บรรทัดแรกคือจำนวน board
- ตามด้วย board state ของแต่ละ board (3 บรรทัดต่อ board)
- Output: ตำแหน่งที่ดีที่สุดสำหรับแต่ละ board

---

## 🧠 Minimax Algorithm

```
         MAX (ผู้เล่น)
        /          \
      MIN (AI)    MIN (AI)
     /    \       /    \
   MAX   MAX    MAX   MAX
   ...   ...    ...   ...
```

**หลักการ:**
1. **Maximizing Player** — เลือก move ที่ได้คะแนนสูงสุด
2. **Minimizing Player** — เลือก move ที่ได้คะแนนต่ำสุด
3. ทำ recursion จนถึง terminal state (ชนะ/แพ้/เสมอ)
4. Backtrack คะแนนกลับขึ้นมาเพื่อหา move ที่ดีที่สุด

## 📁 File Structure

```
week4/
├── README.md                 # ไฟล์นี้
├── coingame.py               # Coin Game (interactive)
├── coingame_first_move.py    # Coin Game (first move check)
├── tictoe.py                 # Tic-Tac-Toe (interactive)
├── tr.py                     # Tic-Tac-Toe (submission)
├── tr copy.py                # Tic-Tac-Toe (batch submission)
└── test.py                   # Test file
```
