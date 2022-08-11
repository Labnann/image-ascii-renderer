BUF=$(python index.py $1)

cat <<EOF
<html>
<body>
<pre style="word-wrap: break-word; white-space: pre-wrap;">
$(echo "$BUF")
</pre>
<script>
document.body.style.zoom=.05
</script>
</body>
</html>
EOF
