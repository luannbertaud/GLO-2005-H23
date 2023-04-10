import CitationCard from "@/components/CitationCard";

export default function Feed() {
  return (
    <div className="grid grid-row-1 gap-12 w-screen h-screen max-h-screen overflow-y-scroll items-center justify-center">
      <CitationCard/>
      <CitationCard/>
      <CitationCard/>
      <CitationCard/>
      <CitationCard/>
    </div>
  )
}
