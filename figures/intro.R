oldpar <- par(no.readonly = TRUE)
oldwd <- getwd()
this.dir <- dirname(parent.frame(2)$ofile)
nombre.R <-  sys.frame(1)$ofile
require(tools)
nombre <- print(file_path_sans_ext(nombre.R))
pdf(paste0(nombre,".pdf"), width = 8, height = 5)
setwd(this.dir)
###############################

par(mar=c(3.75,3.75,0.25,0.25))



delta_expected = 1.5*0.5+0.6*0.5 - 1 # <\Delta x>
time_average = log(1.5)*0.5+log(0.6)*0.5 # <\Delta ln x>



axis(side=2, labels=NA,cex.axis=0.6,tck=0.015)
axis(side=1, labels=NA,cex.axis=0.6,tck=0.015)
axis(lwd=0,side=1, at=0, labels=0,cex.axis=1.25,line=-0.3)
axis(lwd=0,side=1, at=mu[1], labels=expression(mu[a]),cex.axis=1.25,line=-0.85,tck=0.015)
abline(v=mu[1],lty=3)
mtext(text= expression(Skill[a]),side =1,line=2,cex=1.75)
mtext(text ="Density" ,side =2,line=1,cex=1.75)



#######################################
# end 
dev.off()
system(paste("pdfcrop -m '0 0 0 0'",paste0(nombre,".pdf") ,paste0(nombre,".pdf")))
setwd(oldwd)
par(oldpar, new=F)
#########################################
