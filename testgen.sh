#!/bin/bash
DESTBASE="."
export MAINSTUFF="---\ntitle: PCE \nshowinsidebar: true \narticle: false \nicon: category \n---\n";
function urlify(){
  sed -E 's/[^[:alnum:]]+/-/g' <<<"${@,,}";
}
IFS=$'\n'
for item in `cat all.txt | cut -f 2- -d '.' | sed -E 's/^ //g'`;do
  SLUG=$(urlify "${item}")
  DESTBASEDIR=$(urlify "${item}"|colrm 2)
  DESTDIR=$DESTBASE/$DESTBASEDIR
  DESTFILE="${DESTDIR}/${SLUG}.md"
  mkdir -p $DESTDIR
  export INDEXSTUFF="---\ntitle: ${DESTBASEDIR^^} \nshowinsidebar: true \narticle: false \nicon: category \n---\n";
  [[ ! -f $DESTBASE/${DESTBASEDIR}/README.md ]] && printf -- "${INDEXSTUFF}" > $DESTBASE/${DESTBASEDIR}/README.md
  printf -- "1. [${DESTBASEDIR^^}](${DESTBASEDIR})\n" >> $DESTBASE/README.md
  [[ ! `grep ${SLUG} $DESTBASE/${DESTBASEDIR}/README.md` ]] && printf -- "1. [${item}](${SLUG}.html)\n" >> $DESTBASE/${DESTBASEDIR}/README.md
  export STUFF="---\ntitle: ${item} \nshowinsidebar: true \narticle: false \nicon: article \n---\n";
  if [[ ! -f $DESTFILE ]]; then
    echo $DESTFILE
    printf -- "${STUFF}" > $DESTFILE
  fi
done
grep "1. " $DESTBASE/README.md | sort -u > /tmp/all.testgen.txt
printf -- "${MAINSTUFF}" > $DESTBASE/README.md
cat /tmp/all.testgen.txt >> $DESTBASE/README.md

