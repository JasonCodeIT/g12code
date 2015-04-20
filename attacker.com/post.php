<?php

$action = $_GET['action'];
$fields = json_decode($_GET['payload']);
$method = $_GET['method'] ? $_GET['method'] : 'POST';

?>

<form id="proxy" action="<?php echo $action;?>" method="<?php echo $method?>">
<?php foreach($fields as $k => $v):?>
    <input type="hidden" name="<?php echo $k?>" value="<?php echo $v?>" />
<?php endforeach;?>
        <input id="submit" type="submit" value="submit" />
</form>
