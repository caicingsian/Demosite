# 階段式角色工作流

這套 skills 用於 GuildOps 的自主工作流研究。以單一 Agent 依階段切換角色；未設定子 Agent 或背景執行器。

| 階段 | Skill | 進場條件 | 完成／交棒條件 |
|---|---|---|---|
| discovery | product-discovery | 問題或使用者價值不清楚 | 問題與假設可被驗證 |
| definition | mvp-definition | 本輪範圍或完成條件不清楚 | 核心流程與驗收固定 |
| engineering | product-engineering | 已有可實作的明確範圍 | 產品交付且有驗收證據 |
| user_research | user-research | 原型可操作或已有真實回饋 | 回饋整理成下一輪工作 |

MVP 沒有獨立 QA。基本功能驗證與修復是產品工程師的交付責任。
正式多人服務、安全審查與維運等角色，等需求出現再增加。

## 使用方法

Agent 在支援專案 AGENTS.md 的環境開啟 repository 後，先讀入口與 workflow.json，再讀對應 SKILL.md。
若客戶端不自動發現專案 skills，可明確要求它讀 AGENTS.md 及目標 skill。
檔案已放在標準專案位置 .agents/skills/<name>/SKILL.md；執行中的對話可能需要新工作階段才會重新列入 skill catalog。
這套檔案提供可閱讀的調度規則，沒有常駐程序、自動喚醒或排程。

## 每次交棒紀錄

更新 workflow.json：phase、role、status、goal、evidence、next_actions、blockers。
以原始碼、實際驗收結果與使用者回饋為依據；不要只因 skill 已建立就宣稱已驗證其成效。
可新增 iteration 紀錄，包含變更、實際失敗與修復、人工決策及未驗證項目。
沒有收集到的成本／耗時／介入數據應標示 unknown，不補造數字。

## 當前起點

GuildOps MVP 已交付並完成工程驗證，下一階段為使用者研究，等待真實試用回饋。
這四份 skills 是交付 MVP 後建立；不能回溯宣稱前一輪開發已採用這套流程。
