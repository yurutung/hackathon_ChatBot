$(document).ready(function() {

    //Chatbot開頭
    show_chatbot_msg('Chatbot!! </p><p>請選擇功能：')
    chat_bot_options()

    //選擇的功能
    // option1
    $(document).on('click', '#option1', function() {
        show_chatbot_msg('hi~~~~~')
    })
    // option2
    $(document).on('click', '#option2', function() {
        window.open('https://www.google.com.tw/', 'google')
    })

    //get user input message
    $('#send_msg_icon').click(function(){
        msg = $('#send_msg').val()
        if (msg != ''){
            show_user_msg(msg) //顯示在聊天視窗
            $.ajax({
                type : 'POST',
                url : '/get_msg',
                data : JSON.stringify({
                    send_msg : msg
                }),
                dataType: 'json'
            }).done(function (data) {
                if (data.error) {
                    alert('error')
                }
                else {
                    if (data == false) {
                    alert('error')
                    }
                    else {
                        $('#send_msg').val("")
                        show_chatbot_msg(data.res_msg)
                    }
                }
            })
        }
    })

    // 功能選項btn click
    $('#option_btn').click(function(){
        show_chatbot_msg('請選擇功能：')
        chat_bot_options()
    })

})
