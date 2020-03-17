<h1>Flow of client</h1>
<ul><li>App Start</li>
<li>Client initiation(client id generation)</li>
<li>Print menu</li>
<li>Cart generation</li>
<li>Cart total and selection print</li>
<li>Payment initiation</li>
<li>Await payment response</li>
<li>Token generation</li>
<li>Await ack for order completion</li>
<li>Database clean (remove client id and token)</li>
<li>Logging (add the order items and total to server db)</li>
</ul>