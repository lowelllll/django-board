$('#comment_btn').on('click',function(){
    var value = $('#comment_value').val();
    $.ajax({
        type:'POST',
        url:"{% url 'post:comment_create' %}",
        data:{
            'content':value,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
        },
        dataType:'json',
        success:function(response){
            if(response.result == 'success'){
                data = response.data;
                alert('댓글이 저장되었습니다.');
                $(".comment").append(`<li>${data.writer} | ${data.content} | ${data.date}</li>`);
            }
        }
    });
});