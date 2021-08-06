# ChatBot

## Install & Usage
1. run frontend page
    ```
    npm install
    npm start
    ```
2. rasa train
    ```
    npm run train
    ```
3. run rasa bot
    ```
    npm run rasa
    ```
4. run rasa action endpoint
    ```
    npm run action
    ```
5. get into http://localhost:9000

## 功能
當你想要吃某種類型的食物，但公司這麼多廠區、這麼多餐廳，你怎麼知道哪裡有呢! 打開chatbot來問問吧!
### 使用流程
* user input
    * where has (食物種類)
    * where can i buy (食物種類)
    * i want to buy (食物種類)
    * i want to eat (食物種類)
    * i want to drink (食物種類)
* chatbot output
    * (哪一廠區的哪一間店) has (user輸入的食物種類) !
    * you can find (user輸入的食物種類) in (哪一廠區的哪一間店) 😜
    * (user輸入的食物種類) is waiting for you at (哪一廠區的哪一間店) 😊

## code 說明
[domain.yml](https://github.com/yurutung/hackathon_ChatBot/blob/master/domain.yml)
* setting intents
    ```
    intents:
      - search_meal
    ```
* setting actions connect to action endpoint
    ```
    actions:
    - action_check_meal_category
    ```
* setting responses place found or not found
    ```
    responses:
        utter_place_found:
        - text: "{place} has {category}!"
        - text: "you can find {category} in {place} 😜"
        - text: "{category} is waiting for you at {place} 😊"
        utter_place_not_found:
        - text: "Hmm... not found 😤"
        - text: "i did not find this food 😢"
    ```
[data/nlu.yml](https://github.com/yurutung/hackathon_ChatBot/blob/master/data/nlu.yml)
* setting intents examples
    ```
    nlu:
    - intent: search_meal
    examples: |
        - where can i buy [dumplings](meal_category)
        ...
    ```
[data/stories.yml](https://github.com/yurutung/hackathon_ChatBot/blob/master/data/stories.yml)
* setting story
    if get search meal intent, then use action action_check_meal_category
    ```
    stories:
    - story: search meal place
    steps: 
    - intent: search_meal
    - action: action_check_meal_category
    ```
[actions/actions.py](https://github.com/yurutung/hackathon_ChatBot/blob/master/actions/actions.py)
* get user input meal category, get the place, then return the place. if not found, then return not found
    ```
    class ActionCheckMealCategory(Action):
        ...
    ```