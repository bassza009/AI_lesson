import os
import sys


if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdin.reconfigure(encoding='utf-8')
    except Exception:
        pass

def load_knowledge_base(filepath):
    """
    อ่านไฟล์ฐานความรู้ (knowledge.txt) 
    รูปแบบกฎ: Premise1, Premise2 => Conclusion
    """
    rules = []
    if not os.path.exists(filepath):
        print(f"Error: ไม่พบไฟล์ฐานความรู้ {filepath}")
        return rules

    with open(filepath, 'r', encoding='utf-8-sig') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or "=>" not in line:
                continue
            lhs, rhs = line.split("=>", 1)
            premises = [p.strip() for p in lhs.split(",") if p.strip()]
            conclusion = rhs.strip()
            if premises and conclusion:
                rules.append({
                    "id": len(rules) + 1,
                    "premises": set(premises),
                    "conclusion": conclusion,
                    "raw": line
                })
    return rules

def forward_chaining(rules, initial_facts):
    """
    อัลกอริทึม Forward Chaining ในการอนุมานความรู้
    """
    facts = set(initial_facts)
    fired_rules = []
    inferred = True
    
    while inferred:
        inferred = False
        for rule in rules:
            # หากเงื่อนไข (Premises) ทั้งหมดเป็นจริงใน Facts และข้อสรุปยังไม่ได้ถูกเพิ่ม
            if rule["premises"].issubset(facts) and rule["conclusion"] not in facts:
                facts.add(rule["conclusion"])
                fired_rules.append(rule)
                inferred = True
                
    return facts, fired_rules

def get_all_symptoms(rules):
    """
    สกัดรายการอาการที่เป็นปัจจัยป้อนเข้าเริ่มต้น (Premises ที่ไม่ได้เป็น Conclusion ของกฎอื่น)
    """
    all_premises = set()
    all_conclusions = set()
    for rule in rules:
        all_premises.update(rule["premises"])
        all_conclusions.add(rule["conclusion"])
    
    # อาการเริ่มต้นคือ Premise ที่ไม่อยู่ในข้อสรุปของกฎใดๆ
    initial_symptoms = sorted(list(all_premises - all_conclusions))
    return initial_symptoms

def main():
    kb_path = os.path.join(os.path.dirname(__file__), "knowledge.txt")
    rules = load_knowledge_base(kb_path)
    
    if not rules:
        print("ไม่สามารถโหลดฐานความรู้ได้")
        return

    print("=" * 65)
    print("  ระบบผู้เชี่ยวชาญวินิจฉัยปัญหาคอมพิวเตอร์ (KRR - Forward Chaining)")
    print("=" * 65)
    
    symptoms = get_all_symptoms(rules)
    
    print("\n[รายการอาการเสียในฐานความรู้]:")
    for idx, sym in enumerate(symptoms, 1):
        print(f"  {idx:2d}. {sym}")
        
    print("\n" + "-" * 65)
    print("คำแนะนำ: ป้อนหมายเลขอาการเสีย (เช่น 1, 2) หรือพิมพ์ชื่ออาการ (คั่นด้วย , )")
    user_input = input("ระบุอาการเสียที่พบ: ").strip()
    
    if not user_input:
        print("ไม่ได้ระบุอาการเสีย ยุติการทำงาน")
        return

    selected_facts = set()
    tokens = [t.strip() for t in user_input.split(",") if t.strip()]
    for token in tokens:
        if token.isdigit():
            num = int(token)
            if 1 <= num <= len(symptoms):
                selected_facts.add(symptoms[num - 1])
        else:
            selected_facts.add(token)

    if not selected_facts:
        print("ไม่พบอาการเสียที่ถูกต้อง")
        return

    print("\n" + "=" * 65)
    print("📌 อาการเสียตั้งต้น (Initial Facts):")
    for fact in selected_facts:
        print(f"  • {fact}")

    # ทำการประมวลผลด้วย Forward Chaining
    all_facts, fired_rules = forward_chaining(rules, selected_facts)
    new_inferences = all_facts - selected_facts

    print("\n⚙️  ขั้นตอนการอนุมาน (Inference Process):")
    if not fired_rules:
        print("  - ไม่มีการทำงานของกฎใดเพิ่มเติม")
    else:
        for idx, rule in enumerate(fired_rules, 1):
            premises_str = " AND ".join(sorted(rule['premises']))
            print(f"  {idx}. [Rule {rule['id']}] IF ({premises_str}) THEN -> {rule['conclusion']}")

    print("\n" + "=" * 65)
    print("📋 ผลการวินิจฉัยและข้อแนะนำ (Diagnosis Results):")
    print("=" * 65)
    
    if not new_inferences:
        print("❌ ไม่พบข้อวินิจฉัยที่ตรงกับอาการที่ระบุในฐานความรู้")
    else:
        diagnoses = [f for f in new_inferences if f.startswith("สงสัยว่า")]
        recommendations = [f for f in new_inferences if f.startswith("แนะนำให้")]
        others = [f for f in new_inferences if not f.startswith("สงสัยว่า") and not f.startswith("แนะนำให้")]

        if diagnoses:
            print("\n🔍 ข้อวินิจฉัยสาเหตุ:")
            for d in diagnoses:
                print(f"  • {d}")

        if recommendations:
            print("\n💡 คำแนะนำการแก้ไข:")
            for r in recommendations:
                print(f"  • {r}")

        if others:
            print("\n📌 ข้อสรุปเพิ่มเติม:")
            for o in others:
                print(f"  • {o}")
                
    print("\n" + "=" * 65)

if __name__ == "__main__":
    main()
