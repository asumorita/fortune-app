import streamlit as st
import random
from datetime import datetime, timezone, timedelta

# ページ設定
st.set_page_config(
    page_title="今日の運勢占い",
    page_icon="🔮",
    layout="centered"
)

# タイトル
st.title("🔮 今日の運勢占い 🔮")

# 日本時間を取得
jst = timezone(timedelta(hours=9))
now_jst = datetime.now(jst)
st.write(f"📅 {now_jst.strftime('%Y年%m月%d日')}")

# 名前入力
name = st.text_input("あなたの名前を入力してください", placeholder="例：太郎")

# 占いボタン
if st.button("🎯 占う！", type="primary"):
    if name:
        # 今日の日付で乱数のシードを設定
        today = now_jst.strftime("%Y%m%d")
        seed = int(today) + sum(ord(c) for c in name)
        random.seed(seed)
        
        # 総合運
        total_score = random.randint(50, 100)
        stars = "⭐" * ((total_score // 20) + 1)
        
        # メッセージ
        fortune_messages = [
            "🌟 最高の一日になりそう！積極的に行動すると吉",
            "✨ 良い出会いがありそうな予感。人との繋がりを大切に",
            "🎯 チャンスの日！思い切った決断が成功を呼ぶ",
            "💎 金運アップの日。お金に関する良い知らせがあるかも",
            "🍀 穏やかで平和な一日。リラックスして過ごしましょう",
            "⚡ エネルギッシュな日。新しいことに挑戦してみて",
            "🌈 幸運が舞い込む予感。周囲に感謝の気持ちを忘れずに",
            "🎁 思いがけないプレゼントやサプライズがあるかも",
            "💪 やる気がみなぎる日。目標に向かって突き進もう",
            "🌸 心が満たされる出来事がありそう。素直な気持ちで",
        ]
        
        love_fortunes = [
            "💕 恋愛運絶好調！気になる人に連絡してみて",
            "💗 パートナーとの絆が深まる日。素直な気持ちを伝えて",
            "💝 新しい出会いの予感。いつもと違う場所に行ってみて",
            "💖 恋愛運普通。焦らずマイペースで",
            "💓 告白には良い日。勇気を出してみよう",
        ]
        
        work_fortunes = [
            "💼 仕事運最高！大きな成果が期待できる日",
            "📊 アイデアが冴える日。提案してみよう",
            "🎯 目標達成に近づく日。集中して取り組んで",
            "💻 効率アップの日。スムーズに仕事が進む",
            "📈 上司や同僚から評価されそう。積極的に",
        ]
        
        money_fortunes = [
            "💰 金運最高！臨時収入の可能性あり",
            "💸 無駄遣い注意の日。計画的にお金を使って",
            "💴 投資のチャンス。慎重に判断して",
            "💵 節約が実を結ぶ日。将来のために貯蓄を",
            "🪙 お金の良い知らせがありそう",
        ]
        
        lucky_colors = ["赤", "青", "黄色", "緑", "ピンク", "紫", "オレンジ", "白", "黒", "金色"]
        lucky_items = ["スマホ", "ペン", "ノート", "コーヒー", "お茶", "お菓子", "音楽", "本", "財布", "時計"]
        
        advices = [
            "笑顔を忘れずに。あなたの笑顔が幸運を呼びます",
            "困っている人がいたら助けてあげて。良いことが返ってきます",
            "新しいことにチャレンジしてみて。成長のチャンス",
            "感謝の気持ちを言葉にして伝えましょう",
            "健康第一。無理せず休憩も大切に",
        ]
        
        # 結果表示
        st.markdown("---")
        st.header(f"{name}さんの運勢")
        
        # 総合運
        st.subheader(f"✨ 総合運: {total_score}点 {stars}")
        st.write(random.choice(fortune_messages))
        
        # 各運勢を横並びで表示
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💕 恋愛運")
            st.write(random.choice(love_fortunes))
            
            st.markdown("### 💰 金運")
            st.write(random.choice(money_fortunes))
        
        with col2:
            st.markdown("### 💼 仕事運")
            st.write(random.choice(work_fortunes))
        
        # ラッキー情報
        st.markdown("---")
        st.subheader("🍀 今日のラッキー情報")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🎨 カラー", random.choice(lucky_colors))
        with col2:
            st.metric("🎁 アイテム", random.choice(lucky_items))
        with col3:
            st.metric("🔢 ナンバー", random.randint(1, 99))
        
        # アドバイス
        st.markdown("---")
        st.info(f"💡 {random.choice(advices)}")
        
        st.success("素敵な一日をお過ごしください！✨")
        
    else:
        st.warning("名前を入力してください！")

# フッター
st.markdown("---")
st.caption("Created with ❤️ by Streamlit")
