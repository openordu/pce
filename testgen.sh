#!/bin/bash
DESTBASE="."
export MAINSTUFF="---\ntitle: PCE \nindex: 9999 \narticle: false \nicon: category \n---\n";
function urlify(){
  sed -E 's/[^[:alnum:]]+/-/g' <<<"${@,,}";
}
IFS=$'\n'
myarray=(`cat all.txt | cut -f 2- -d '.' | sed -E 's/^ //g'`)

for i in ${!myarray[@]};do
  prev=$(($i - 1))
  next=$(($i + 1))
  echo "${myarray[$prev]}#${myarray[$i]}#${myarray[$next]}"
  SLUG=$(urlify "${myarray[$i]}")
  NEXTSLUG=$(urlify "${myarray[$next]}")
  PREVSLUG=$(urlify "${myarray[$prev]}")
  LETTERBASEDIR=$(urlify "${myarray[$i]}"|colrm 2)
  LETTERDIR=$DESTBASE/$LETTERBASEDIR
  SLUGFILE="${LETTERDIR}/${SLUG}.md"
  mkdir -p $LETTERDIR
  export INDEXSTUFF="---\ntitle: ${LETTERBASEDIR^^} \nindex: "$i"\narticle: false \nicon: folder \n---\n";
  [[ ! -f $DESTBASE/${LETTERBASEDIR}.md ]] && printf -- "${INDEXSTUFF}" > $DESTBASE/${LETTERBASEDIR}.md
  printf -- "1. [${LETTERBASEDIR^^}](${LETTERBASEDIR})\n" >> $DESTBASE/README.md
  [[ ! `grep ${SLUG} $DESTBASE/${LETTERBASEDIR}.md` ]] && printf -- "1. [${myarray[$i]}](${LETTERBASEDIR}/${SLUG}.md)\n" >> $DESTBASE/${LETTERBASEDIR}.md
  export STUFF="---\ntitle: ${myarray[$i]} \nindex: false\narticle: false \nicon: article\nnext: $NEXTSLUG.md\nprev: $PREVSLUG.md\n---\n";
  if [[ ! -f $SLUGFILE ]]; then
    echo $SLUGFILE
    printf -- "${STUFF}" > $SLUGFILE
  fi
done

grep "1. " $DESTBASE/README.md | sort -u > /tmp/all.testgen.txt
printf -- "${MAINSTUFF}" > $DESTBASE/README.md
cat /tmp/all.testgen.txt >> $DESTBASE/README.md
