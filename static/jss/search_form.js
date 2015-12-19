$(function(){
    var obj = $(".views-exposed-form");

    function enterButton(obj){
        $("input[name=trg]").css(
            {
                "width":150,
                "display": "block",
                "padding":"0 0 0 5px",
            }
        );
    };

    function leaveButton(obj){
        $("input[name=trg]").css(
            {
                "padding": 0,
                "width":0, 
                "display": "none",
            }
        );
    };

    obj.mouseenter(function(){
        enterButton(this);
    });

    obj.mouseleave(function(){
        leaveButton(this);
    });

});
