(function($) {
    $(document).ready(function($) {
        $(".sortable").sortable({
            update: function() {
                set_ids();
            }
        });
        set_ids();
    });
    
    function set_ids() {
        var first = true;
        var id_list = "";
        $(".sortable li").each(function() {
            if (first) {
                id_list = $(this).attr("value");
            }
            else {
               id_list += "," + $(this).attr("value"); 
            }
            first = false;
        })
        $(".sortable-submit").val(id_list);
    }
    
})(jQuery.noConflict());