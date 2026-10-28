import streamlit as st
import pandas as pd

st.set_page_config(page_title="TCS RCA Tool")
st.title("A0-03: RCA Tool for Service Company")
st.subheader("Service Company: TCS | Client: SBI YONO")
st.caption("Real Incident: 26 Oct 2026 - 02:14 AM Crash, 02:55 AM Restored")
st.info("READ-ONLY Tool | Follows KG Workflow")

if st.button("ANALYZE GHOST INCIDENT", type="primary"):
    st.header("1. Detect & 2. Collect Evidence")
    data = [
        ["02:00:00", "TCS deployed patch v2.4", "INFO"],
        ["02:13:50", "Memory 89%", "WARN"],
        ["02:14:03", "OOMKilled - Memory 98%", "ERROR"],
        ["02:14:05", "DB Timeout - Pool exhausted", "ERROR"],
        ["02:55:00", "Restarted - Restored", "INFO"],
    ]
    df = pd.DataFrame(data, columns=["Timestamp", "Message", "Level"])
    st.dataframe(df, use_container_width=True)

    st.header("3. Timeline: BEFORE / DURING / AFTER")
    st.code("BEFORE 02:00 Deploy -> DURING 02:14 OOMKilled -> AFTER 02:55 Restart")

    st.header("4. Rank Root Causes WITH EVIDENCE")
    st.success("RANK 1: Memory Leak due to Unclosed DB - 92%")
    st.write("Evidence 1: Log says OOMKilled Memory 98% at 02:14:03")
    st.write("Evidence 2: Memory 45% to 98% in 14 mins after deployment")
    st.write("Evidence 3: Crash 14 mins after deployment")

    st.warning("RANK 2: DB Connection Leak - 68%")
    st.write("Evidence: DB Timeout right after memory full")

    st.header("5. Explain Why")
    st.write("Patch v2.4 did not close DB connections. Memory full and crashed. Restart cleared memory but bug remains.")

    st.header("6. Preventive Actions for SBI Client Report")
    st.write("1. Fix code to close DB connections")
    st.write("2. Set memory alert at 80%")
    st.write("3. Add auto-scaling")
    st.write("4. Deployment check before release")

st.write("Workflow: Detect -> Collect Logs -> Timeline -> Rank with Evidence -> Explain -> Prevent")
