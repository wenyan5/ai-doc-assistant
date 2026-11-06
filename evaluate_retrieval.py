from retrieval import search_documents


TEST_CASES = [
    ("NovaDesk 支持 Linux 吗？", "installation.md"),
    ("一个账户最多可以激活几台电脑？", "installation.md"),
    ("编辑者可以修改其他成员的角色吗？", "permissions.md"),
    ("查看者什么时候可以下载 PDF？", "permissions.md"),
    ("专业版按年付款时每名成员每月多少钱？", "pricing.md"),
    ("出现 E410 错误应该怎么处理？", "error-codes.md"),
    ("删除应用会自动取消订阅吗？", "cancellation.md"),
    ("年度方案购买10天后取消可以全额退款吗？", "cancellation.md"),
    ("谁可以导出整个工作区？", "data-export.md"),
    ("数据导出链接多长时间后过期？", "data-export.md"),
]


correct_count = 0

for number, (question, expected_source) in enumerate(TEST_CASES, start=1):
    results = search_documents(question)
    sources = [result["filename"] for result in results]
    passed = expected_source in sources

    if passed:
        correct_count += 1

    status = "PASS" if passed else "FAIL"

    print(f"{number}. {status}")
    print(f"   Question: {question}")
    print(f"   Expected: {expected_source}")
    print(f"   Top 3: {sources}")

print(f"\nResult: {correct_count}/{len(TEST_CASES)} correct sources in top 3")