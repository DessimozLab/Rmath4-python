from setuptools import setup, Extension

setup(
    py_modules=['Rmath'],
    ext_modules=[Extension('_Rmath',
        language='c',
        define_macros=[('MATHLIB_STANDALONE', None)],
        include_dirs=['include'],
        sources=[
            'src/standalone/sunif.c',
            'src/bd0.c',
            'src/bessel_i.c',
            'src/bessel_j.c',
            'src/bessel_k.c',
            'src/bessel_y.c',
            'src/beta.c',
            'src/chebyshev.c',
            'src/choose.c',
            'src/cospi.c',
            'src/d1mach.c',
            'src/dbeta.c',
            'src/dbinom.c',
            'src/dcauchy.c',
            'src/dchisq.c',
            'src/dexp.c',
            'src/df.c',
            'src/dgamma.c',
            'src/dgeom.c',
            'src/dhyper.c',
            'src/dlnorm.c',
            'src/dlogis.c',
            'src/dnbeta.c',
            'src/dnbinom.c',
            'src/dnchisq.c',
            'src/dnf.c',
            'src/dnorm.c',
            'src/dnt.c',
            'src/dpois.c',
            'src/dt.c',
            'src/dunif.c',
            'src/dweibull.c',
            'src/expm1.c',
            'src/fmax2.c',
            'src/fmin2.c',
            'src/fprec.c',
            'src/fround.c',
            'src/fsign.c',
            'src/ftrunc.c',
            'src/gamma.c',
            'src/gamma_cody.c',
            'src/gammalims.c',
            'src/i1mach.c',
            'src/imax2.c',
            'src/imin2.c',
            'src/lbeta.c',
            'src/lgamma.c',
            'src/lgammacor.c',
            'src/log1p.c',
            'src/mlutils.c',
            'src/pbeta.c',
            'src/pbinom.c',
            'src/pcauchy.c',
            'src/pchisq.c',
            'src/pexp.c',
            'src/pf.c',
            'src/pgamma.c',
            'src/pgeom.c',
            'src/phyper.c',
            'src/plnorm.c',
            'src/plogis.c',
            'src/pnbeta.c',
            'src/pnbinom.c',
            'src/pnchisq.c',
            'src/pnf.c',
            'src/pnorm.c',
            'src/pnt.c',
            'src/polygamma.c',
            'src/ppois.c',
            'src/pt.c',
            'src/ptukey.c',
            'src/punif.c',
            'src/pweibull.c',
            'src/qbeta.c',
            'src/qbinom.c',
            'src/qcauchy.c',
            'src/qchisq.c',
            'src/qexp.c',
            'src/qf.c',
            'src/qgamma.c',
            'src/qgeom.c',
            'src/qhyper.c',
            'src/qlnorm.c',
            'src/qlogis.c',
            'src/qnbeta.c',
            'src/qnbinom.c',
            'src/qnchisq.c',
            'src/qnf.c',
            'src/qnorm.c',
            'src/qnt.c',
            'src/qpois.c',
            'src/qt.c',
            'src/qtukey.c',
            'src/qunif.c',
            'src/qweibull.c',
            'src/rbeta.c',
            'src/rbinom.c',
            'src/rcauchy.c',
            'src/rchisq.c',
            'src/rexp.c',
            'src/rf.c',
            'src/rgamma.c',
            'src/rgeom.c',
            'src/rhyper.c',
            'src/rlnorm.c',
            'src/rlogis.c',
            'src/rmultinom.c',
            'src/rnbinom.c',
            'src/rnchisq.c',
            'src/rnorm.c',
            'src/rpois.c',
            'src/rt.c',
            'src/runif.c',
            'src/rweibull.c',
            'src/sexp.c',
            'src/sign.c',
            'src/signrank.c',
            'src/snorm.c',
            'src/stirlerr.c',
            'src/toms708.c',
            'src/wilcox.c',
        ],
    )],
)
