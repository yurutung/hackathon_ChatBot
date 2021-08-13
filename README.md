# 執行
1. pip install rasa (未安裝rasa請先安裝) : 
    `pip3 install --index-url http://packagenexus.tsmc.com.tw/repository/python-proxy-group/simple/ --trusted-host packagenexus.tsmc.com.tw --default-timeout 300 rasa`
2. run rasa :
    `rasa run -m models --enable-api --cors "*"`
3. run rasa actions :
    `rasa run actions`
4. open `index.html` and you can see rasa bot
    >:warning: you can also run `node app.js` but you cannot see myTSMC3.0 image in website(可能是公司會擋掉!!)
