git clone https://bitbucket.org/taccaci/foundation-cli.git agave-cli
git clone https://github.com/iPlantCollaborativeOpenSource/iplant-agave-sdk.git --recursive

echo "export IPLANT_SDK_HOME=$PWD/iplant-agave-sdk" >> ~/.profile
echo "PATH=\$PATH:\$IPLANT_SDK_HOME/scripts:" >> ~/.profile
echo "export AGAVE_SDK_HOME=$PWD/agave-cli" >> ~/.profile
echo "export PATH=\$PATH:\$AGAVE_SDK_HOME/bin" >> ~/.profile
source ~/.profile
tenants-init -t iplantc.org

clients-create -S -v -N my_client -D "Client Testing"
auth-tokens-create -S -v
echo User Work Directory: $WORK
iplant-systems-create