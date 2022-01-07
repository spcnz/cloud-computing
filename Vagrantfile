Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", path:"install-docker.sh"
  config.vm.provision "shell", path:"install-docker-compose.sh"
  config.vm.provision "shell", path:"export_env.sh"
  config.vm.network :forwarded_port, host: 8001, guest: 8001
  config.vm.network :forwarded_port, host: 8002, guest: 8002
  config.vm.provision "file", source: ".", destination: "app"
  config.vm.provision "shell", path:"start-app.sh"
end
