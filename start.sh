tmux new-session -s 'mc' -n 'server' -d java -Xmx7000m -Xms1024m -Dfml.readTimeout=200 -jar ~/MCserver/fabric-server-launch.jar nogui
