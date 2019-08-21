import ProjectCard from '../../src/components/sub-layout/project-card.vue';
import Vue from 'vue';


describe('project-card', () => {

  // got props ?
  it('should have a prop called project', () => {
    const propName = Object.keys(ProjectCard.props).filter( key => key === 'project').join('');
    expect(propName).toBe('project');
  });

  it('should have project prop to be a function', () => {
    expect(typeof ProjectCard.props.project).toBe("object");
  });

  it('should one component called carousel', () => {
    const carousel = ProjectCard.components.Carousel.name;
    expect(carousel).toBe('carousel');
  });

  it('should one component called slide', () => {
    const slide = ProjectCard.components.Slide.name;
    expect(slide).toBe('slide');
  });
});
