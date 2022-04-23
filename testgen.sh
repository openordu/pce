#!/bin/bash
DESTBASE="."
export MAINSTUFF="---\ntitle: PCE \nindex: 9999 \narticle: false \nicon: category \n---\n";
function urlify(){
  sed -E 's/[^[:alnum:]]+/-/g' <<<"${@,,}";
}
IFS=$'\n'
index=9999
for item in `cat all.txt | cut -f 2- -d '.' | sed -E 's/^ //g'`;do
  index=$((index - 1))
  SLUG=$(urlify "${item}")
  LETTERBASEDIR=$(urlify "${item}"|colrm 2)
  LETTERDIR=$DESTBASE/$LETTERBASEDIR
  SLUGFILE="${LETTERDIR}/${SLUG}.md"
  mkdir -p $LETTERDIR
  export INDEXSTUFF="---\ntitle: ${LETTERBASEDIR^^} \nindex: "$index"\narticle: false \nicon: category \n---\n";
  [[ ! -f $DESTBASE/${LETTERBASEDIR}.md ]] && printf -- "${INDEXSTUFF}" > $DESTBASE/${LETTERBASEDIR}.md
  printf -- "1. [${LETTERBASEDIR^^}](${LETTERBASEDIR})\n" >> $DESTBASE/README.md
  [[ ! `grep ${SLUG} $DESTBASE/${LETTERBASEDIR}.md` ]] && printf -- "1. [${item}](${LETTERBASEDIR}/${SLUG}.md)\n" >> $DESTBASE/${LETTERBASEDIR}.md
  export STUFF="---\ntitle: ${item} \nindex: false\narticle: false \nicon: article \n---\n";
  if [[ ! -f $SLUGFILE ]]; then
    echo $SLUGFILE
    printf -- "${STUFF}" > $SLUGFILE
  fi
done
grep "1. " $DESTBASE/README.md | sort -u > /tmp/all.testgen.txt
printf -- "${MAINSTUFF}" > $DESTBASE/README.md
cat /tmp/all.testgen.txt >> $DESTBASE/README.md
