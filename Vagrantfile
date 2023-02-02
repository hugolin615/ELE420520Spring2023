

Vagrant.configure("2") do |config|
  config.vm.box = "hugolin615/ELE420"
  config.vm.box_version = "1.0"
  
  config.vm.provider "virtualbox" do |v|
	v.name = "ELE420520" + Time.now.strftime(" %Y-%m-%d")
  end
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
    vb.memory = 2048
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--vram", "32"]
  end
end
