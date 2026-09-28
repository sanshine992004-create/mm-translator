import streamlit as st
from deep_translator import GoogleTranslator

# အက်ပ်ခေါင်းစဉ်
st.set_page_config(page_title="Chinese to Myanmar Subtitle Translator", page_icon="🈲")

st.title("🈲 တရုတ်မှ မြန်မာ စာတန်းထိုး ဘာသာပြန်စနစ်")
st.write("တရုတ် ဗီဒီယိုလင့်ခ် သို့မဟုတ် စာသားများကို ထည့်သွင်းပြီး မြန်မာလို ဘာသာပြန်ဆိုနိုင်ပါသည်။")

# အသုံးပြုသူထံမှ ထည့်သွင်းမှု ရယူရန်
input_type = st.radio("ဘာသာပြန်မည့် ပုံစံကို ရွေးပါ:", ["ဗီဒီယို လင့်ခ် (Link)", "တရုတ်စာသား (Text)"])

if input_type == "ဗီဒီယို လင့်ခ် (Link)":
    video_link = st.text_input("တရုတ် ဗီဒီယို လင့်ခ်ကို ထည့်ပါ (ဥပမာ - YouTube / Douyin / ฯลฯ):")
    if st.button("ဗီဒီယို စာတန်းများကို ဖတ်ရှုမည်"):
        if video_link:
            st.info("ဗီဒီယိုအချက်အလက်များကို ချိတ်ဆက်နေပါပြီ...")
            st.success("လင့်ခ် ရရှိပါပြီ။ ကျေးဇူးပြု၍ အောက်ပါ စာသားဘောက်စ်တွင် တရုတ်စာသားများကို ထည့်သွင်းပေးပါ။")
        else:
            st.warning("ကျေးဇူးပြု၍ လင့်ခ်ထည့်ပါ။")

else:
    chinese_text = st.text_area("ဘာသာပြန်လိုသော တရုတ်စာသားများကို ဤနေရာတွင် ကူးထည့်ပါ (Paste):")
    if st.button("မြန်မာလို ဘာသာပြန်မည်"):
        if chinese_text:
            with st.spinner("မြန်မာဘာသာသို့ ဘာသာပြန်ဆိုနေပါပြီ..."):
                try:
                    # Google Translate ကို အသုံးပြု၍ တရုတ်မှ မြန်မာသို့ ဘာသာပြန်ခြင်း
                    translated_text = GoogleTranslator(source='zh-CN', target='my').translate(chinese_text)
                    
                    st.subheader("📝 မူရင်း တရုတ်စာသား:")
                    st.code(chinese_text, language='text')
                    
                    st.subheader("🇲🇲 မြန်မာဘာသာပြန်:")
                    st.success(translated_text)
                except Exception as e:
                    st.error(f"အမှားအယွင်းရှိသည်: {e}")
        else:
            st.warning("ကျေးဇူးပြု၍ ဘာသာပြန်မည့် စာသားများကို ထည့်ပါ။")
          
