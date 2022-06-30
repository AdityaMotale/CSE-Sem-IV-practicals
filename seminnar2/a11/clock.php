<head>
    <style>

       p{
           color:yellow;
           font-size: 90px;
           position: absolute;
           top: 40%;
           bottom: 50%;
       }
       body{
           background-color: brown;
       }
        </style>
        <body>
            <p>
                <?php 
                
                date_default_timezone_set("Asia/Kolkata");
                echo date("h:i:sA");
                ?>
            </p>
        </body>
</head>