JMdist2 <- function(g,X){

  X<-as.matrix(X)

  nfeat <- ncol(X)
  nclass <- length(unique(g))

  mu <- by(X,g,colMeans)

  Cov <- by(X,g,stats::cov)

  ncomb <- t(utils::combn(unique(g),2))
  Bhat <- c()
  jm <- c()
  for(j in 1:nrow(ncomb)){
    mu.i <- mu[[ncomb[j,1]]]
    cov.i <- Cov[[ncomb[j,1]]]
    mu.j <- mu[[ncomb[j,2]]]
    cov.j <- Cov[[ncomb[j,2]]]
    if(nfeat==1){
      Bhat[j]<-(1/8)*t(mu.i-mu.j) %*% (solve((cov.i+cov.j)/2)) %*% (mu.i-mu.j) + 0.5*log((((cov.i+cov.j)/2))/(sqrt((cov.i))*sqrt((cov.j))),base=exp(1))
    }else{
      Bhat[j]<-(1/8)*t(mu.i-mu.j) %*% (solve((cov.i+cov.j)/2)) %*% (mu.i-mu.j) + 0.5*log(det(((cov.i+cov.j)/2))/(sqrt(det(cov.i))*sqrt(det(cov.j))),base=exp(1))
    }
    jm[j] <- (2*(1-exp(-Bhat[j])))
  }

  return(list(classComb=ncomb,jmdist=jm))

}