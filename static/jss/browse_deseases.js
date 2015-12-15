$(function(){
    
    var list = $("#deseases-in-category");
    var url_prefix = "";
    
    list.html();
    getData();
    
    function getData(){
        $.ajax({
            method: "GET",
            url: $("#desease-browse-link").attr("moveto"),
            dataType: "json",
            success: function(data){
                var d = $.parseJSON(data);
                for(a=0;a<d.length;a++){
                    list.append(insertData(d[a]));
                    };
                return false;
            },
        });
    };
    
    function insertData(i){
        var row = "<li><a href=\""+ url_prefix + i["link"] +"\">"+ i["inner_name"];
        var chl = i["children"].length;
        if(chl > 0){
                row += insertChildren(i["children"]);
            };
        row += "</li>";
        return row;
    };
    
    function insertChildren(children){
        var ul = "<ul>";
        $(children).each(function(){
            var li = "<li>";
            li += "<a href=\""+ url_prefix + this.link +"\">"+ this.inner_name +"</a>";
            li += insertChildren(this.children);
            li += "</li>";
            ul += li;
        });
        /*
        for(b=0;b<children.length;b++){
            var li = "<li>";
            li += "<a href=\""+ children[b].link +"\">"+ children[b].inner_name +"</a>";
            li += insertChildren(children[b]["children"]);
            li += "</li>";
            ul += li;
            };
        */
        ul += "</ul>";
        return ul;
        };
    
    /*
    $("#desease-browse-link").click(function(){
        getData();
        return false;
        });
    */
});
