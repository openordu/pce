#!/bin/bash
DESTBASE="."
export MAINSTUFF="---\ntitle: PCE \nshowinsidebar: true \narticle: false \nicon: category \n---\n";
function urlify(){
  sed -E 's/[^[:alnum:]]+/-/g' <<<"${@,,}";
}
IFS=$'\n'
i=4000
for item in `cat all.txt | cut -f 2- -d '.' | sed -E 's/^ //g'`;do
  i=$(expr $i - 1)
  echo $i
  SLUG=$(urlify "${item}")
  DESTBASEDIR=$(urlify "${item}"|colrm 2)
  DESTDIR=$DESTBASE/$DESTBASEDIR
  DESTFILE="${DESTDIR}/README.md"
  #mkdir -p $DESTDIR
  export INDEXSTUFF="---\ntitle: ${DESTBASEDIR^^} \nshowinsidebar: true \narticle: false \nicon: category \nautoSort: ${i}\n---\n";
  [[ ! -f $DESTBASE/${DESTBASEDIR}.md ]] && printf -- "${INDEXSTUFF}" > $DESTBASE/${DESTBASEDIR}.md
  printf -- "1. [${DESTBASEDIR^^}](${DESTBASEDIR})\n" >> $DESTBASE/README.md
  [[ ! `grep ${item} $DESTBASE/${DESTBASEDIR}.md` ]] && printf -- "## ${item}\n" >> $DESTBASE/${DESTBASEDIR}.md
  # export STUFF="---\ntitle: ${item} \nshowinsidebar: true \narticle: false \nicon: article \n---\n";
done
grep "1. " $DESTBASE/README.md | sort -u > /tmp/all.testgen.txt
printf -- "${MAINSTUFF}" > $DESTBASE/README.md
cat /tmp/all.testgen.txt >> $DESTBASE/README.md
