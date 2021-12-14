Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", path:"install-docker.sh"
  config.vm.provision "file", source: ".", destination: "app"
  config.vm.provision "shell", path:"export_env.sh"
end
