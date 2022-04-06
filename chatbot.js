<script type=text/javascript>
        $(function() {
          $('a#clearLogButton').on('click', function(e) {
            e.preventDefault()
            $.getJSON('/clearChatlog',
                function(data) {
              //do nothing
            });
            return false;
          });
        });
</script>