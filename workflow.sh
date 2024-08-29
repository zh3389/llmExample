docker build -t basellm:latest .
docker save -o basellm.tar basellm
scp basellm.tar root@43.142.4.76:/root
docker run -p 80:7860 -d basellm:latest
