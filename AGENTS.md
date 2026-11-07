# GuildOps 階段工作流

本專案以 GuildOps 工會績效考核系統為成品，研究 AI 自主交付。
開始工作時先讀 research/workflow.json、research/WORKFLOW.md，依目前工作與階段讀取 .agents/skills 中對應的 SKILL.md。
使用者最新指示與已授權範圍優先；階段交棒不是向使用者重新取得許可的要求。

- 先核對現況與證據，再決定進場角色。單一 Agent 切換角色即可；不自行建立子 Agent。
- discovery → definition → engineering → user_research 為建議流程，可根據證據返回前一階段。
- 已明確的需求不重複訪談、已完成的驗收不重複執行；只做本輪需要的工作。
- MVP 不設獨立 QA 角色。產品工程師對核心流程、資料保存及發布驗證負責。
- 每次交棒更新 workflow.json 的角色、階段、證據、待辦與阻塞；記錄狀態必須符合事實。
- 若需使用者決定，先完成可獨立推進的工作；已有授權不重問。真實績效／獎金制度、付費服務、敏感資料及超出範圍的變更不可自行定案。
- 公開 repository 與瀏覽器 localStorage 不保存真實人事資料、憑證或未經授權的私人訪談。
- skill 是方法與規則，不是背景程序；不得宣稱檔案已使 Agent 自動喚醒或持續執行。
